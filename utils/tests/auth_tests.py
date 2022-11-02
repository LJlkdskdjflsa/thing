from typing import Optional
from django.test import TestCase
from django.contrib.auth.models import Group, User, Permission
import pytest


@pytest.fixture(scope="module")
def app_user_group(django_db_blocker) -> Group:
    with django_db_blocker.unblock():
        group = Group.objects.create(name="app_user")
        change_user_permissions = Permission.objects.filter(
            codename__in=["change_user", "view_user"],
        )
        group.permissions.add(*change_user_permissions)
        return group


@pytest.fixture(scope="module")
def app_user_factory(django_db_blocker, app_user_group: Group):
    """factory as fixture pattern: The factory fixture creates a closure
    which provides the inner function with access to fixtures."""

    # Closure
    def create_user(
        username: str,
        password: Optional[str] = None,
        first_name: Optional[str] = "first name",
        last_name: Optional[str] = "last name",
        email: Optional[str] = "foo@bar.com",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = True,
        groups: list[Group] = [],
    ) -> User:
        """Create User Factory Function

        Args:
            username (str):username
            password (Optional[str], optional): password. Defaults to None.
            first_name (Optional[str], optional): first_name. Defaults to "first name".
            last_name (Optional[str], optional): last_name. Defaults to "last name".
            email (Optional[str], optional): email. Defaults to "foo@bar.com".
            is_staff (bool, optional): is staff or not. Defaults to False.
            is_superuser (bool, optional): is superuser or not. Defaults to False.
            is_active (bool, optional): is active or not. Defaults to True.
            groups (list[Group], optional): the user group. Defaults to [].

        Returns:
            User: user instance generated
        """
        with django_db_blocker.unblock():
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_staff=is_staff,
                is_superuser=is_superuser,
                is_active=is_active,
            )
            user.groups.add(app_user_group)
            # Add additional groups, if provided.
            user.groups.add(*groups)
            return user

    return create_user


@pytest.fixture(scope="module")
def user_A(django_db_blocker, app_user_factory) -> User:
    with django_db_blocker.unblock():
        return app_user_factory("A")


@pytest.fixture(scope="module")
def user_B(django_db_blocker, app_user_factory) -> User:
    with django_db_blocker.unblock():
        return app_user_factory("B")


def test_should_create_user(db, user_A: User, app_user_group: Group) -> None:
    assert user_A.username == "A"
    assert user_A.email == "foo@bar.com"
    assert user_A.groups.filter(pk=app_user_group.pk).exists()


def test_should_create_two_users(db, user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk


def test_should_check_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True


def test_should_not_check_unusable_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False
