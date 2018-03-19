from mlbpool.data.dbsession import DbSessionFactory
from mlbpool.data.account import Account


def admin_check():
    """Create a check that only the user who is True in the AccountInfo database with is_superuser can access
    the admin pages.  Make sure mlbpool/data/config.py has an email assigned that matches the user during
    registration"""
    session = DbSessionFactory.create_session()
    su__query = session.query(Account.id).filter(Account.is_super_user == 1) \
        .filter(Account.id == self.logged_in_user_id).first()
    print(su__query)

    if not su__query[0] == self.logged_in_user_id:
        print("You must be an administrator to view this page")
        self.redirect('/home')

    session.close()


class AccountService:
    @staticmethod
    def get_all_accounts():
        session = DbSessionFactory.create_session()
        account_list = session.query(Account).all()

        session.close()

        return account_list

    @classmethod
    def update_admin(cls, new_admin: str):

        session = DbSessionFactory.create_session()

        for player in session.query(Account.id).filter(Account.id == new_admin):
            session.query(Account.id).filter(Account.id == new_admin).update({"is_super_user": 1})

        session.commit()
        session.close()
