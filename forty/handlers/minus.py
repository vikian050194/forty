class HelpHandler(BaseHandler):
    @property
    def key(self):
        return 

    def handle(self, options: List[str]):
        actions = load_actions()
        time = timedelta(seconds=options)
        if not actions:
            return
        last_action = actions[-1]
        last_action.timestamp = last_action.timestamp - time
        save_actions(actions)


__all__ = ["HelpHandler"]
