def after_scenario(context, scenario):
    if hasattr(context, "note_id"):
        context.api.delete_note(context.note_id)