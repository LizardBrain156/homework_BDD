import requests

class NotesAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_note(self, title=None, content=None):
        response = requests.post(self.base_url, json={"title": title, "content": content})
        return response

    def get_all_notes(self):
        response = requests.get(self.base_url)
        return response

    def get_note(self, note_id):
        response = requests.get(f'{self.base_url}/{note_id}')
        return response

    def edit_note(self, note_id, title, content):
        response = requests.put(f'{self.base_url}/{note_id}', json={"title": title, "content": content})
        return response

    def delete_note(self, note_id):
        response = requests.delete(f'{self.base_url}/{note_id}')
        return response
