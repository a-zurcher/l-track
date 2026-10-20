from typing import ClassVar

from textual.app import App

from app.views.description_prompt_view import DescriptionPromptView
from app.views.project_selector_view import ProjectSelectorView
from app.views.timer_view import TimerView


class ProjectTimerApp(App):
    TITLE = "Project Tracker"
    CSS_PATH = "app/app.tcss"
    SCREENS: ClassVar = {
        "project-selector": ProjectSelectorView,
        "timer": TimerView,
        "description-prompt": DescriptionPromptView
    }

    def on_mount(self):
        self.push_screen(ProjectSelectorView())

if __name__ == "__main__":
    ProjectTimerApp().run()
