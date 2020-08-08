import bilibiliuploader.core as core
import json


class BilibiliUploader():
    def __init__(self):
        self.access_token = None
        self.refresh_token = None
        self.sid = None
        self.mid = None

    def login(self, username, password):
        self.access_token, self.refresh_token, self.sid, self.mid, _ = core.login(username, password)

    def login_by_access_token(self, access_token, refresh_token=None):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.sid, self.mid, _ = core.login_by_access_token(access_token)

    def login_by_access_token_file(self, file_name):
        with open(file_name, "r") as f:
            login_data = json.loads(f.read())
        self.access_token = login_data["access_token"]
        self.refresh_token = login_data["refresh_token"]
        self.sid, self.mid, _ = core.login_by_access_token(self.access_token)

    def save_login_data(self, file_name=None):
        login_data = json.dumps(
            {
                "access_token": self.access_token,
                "refresh_token": self.refresh_token
            }
        )
        try:
            with open(file_name, "w+") as f:
                f.write(login_data)
        finally:
            return login_data


    def upload(self,
               parts,
               copyright: int,
               title: str,
               tid: int,
               tag: str,
               desc: str,
               source: str = '',
               cover: str = '',
               no_reprint: int = 0,
               open_elec: int = 1,
               max_retry: int = 5,
               thread_pool_workers: int = 1):
        return core.upload(self.access_token,
                    self.sid,
                    self.mid,
                    parts,
                    copyright,
                    title,
                    tid,
                    tag,
                    desc,
                    source,
                    cover,
                    no_reprint,
                    open_elec,
                    max_retry,
                    thread_pool_workers)
