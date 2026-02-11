from behave import given, when, then
from tests.test_notesAPI import NotesAPI


# ---------- GIVEN ----------

@given('Notes API is running')
def api_running(context):
    context.api = NotesAPI(base_url="http://127.0.0.1:8000/notes")


@given('at least one note exists')
def make_sure_there_is_a_note(context):
    response = context.api.create_note(
        title="title",
        content="content"
    )
    assert response.status_code == 200

    # сохраняем id созданной заметки
    context.note_id = response.json()["id"]


# ---------- WHEN ----------

@when('user posts a valid note with title "{title}" and content "{content}"')
def post_valid_note(context, title, content):
    context.response = context.api.create_note(title, content)
    context.note_id = context.response.json().get("id")


@when('user posts an invalid note')
def post_invalid_note(context):
    context.response = context.api.create_note()


@when("user requests the list of their notes")
def get_notes(context):
    context.response = context.api.get_all_notes()


@when('user requests this note')
def get_specific_note(context):
    context.response = context.api.get_note(context.note_id)


@when('user sends edited note')
def edit_note(context):
    context.response = context.api.edit_note(
        context.note_id,
        title="edited_title",
        content="edited_content"
    )


@when('user deletes the note')
def delete_note(context):
    context.response = context.api.delete_note(context.note_id)

@when('user searches a note by non-existent ID')
def search_invalid_note(context):
    context.response = context.api.get_note((search_max_id(context)))

@when('user sends edited non-existent note')
def edit_non_existent_note(context):
    context.response = context.api.edit_note((search_max_id(context)), title="edited_title", content="edited_content")

@when('user deletes non-existent note')
def delete_non_existent_note(context):
    context.response = context.api.delete_note(search_max_id(context))


# ---------- THEN ----------

@then('response status code is 200')
def response_status_code_200(context):
    assert context.response.status_code == 200


@then('response status code is 422')
def response_status_code_422(context):
    assert context.response.status_code == 422


@then("existing notes are sent to them")
def show_existing_notes(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)


@then('it is shown to them')
def note_is_shown(context):
    assert context.response.status_code == 200
    assert context.response.json()["id"] == context.note_id


@then('edited note is shown')
def edited_note_is_shown(context):
    data = context.response.json()

    assert context.response.status_code == 200
    assert data["id"] == context.note_id
    assert data["title"] == "edited_title"
    assert data["content"] == "edited_content"


@then('the note is deleted')
def note_is_deleted(context):
    assert context.response.status_code == 200

@then('response status code is 404')
def response_status_code_404(context):
    assert context.response.status_code == 404

def search_max_id(context):
    response = context.api.get_all_notes()
    notes = response.json()
    if notes:
        max_id = 0
        for note in notes:
            if note["id"] > max_id:
                max_id = note["id"]
        return max_id + 1
    else:
        return 1