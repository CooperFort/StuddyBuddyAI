import random

class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            "high_urgency": [
                "Break this task into smaller subtasks and focus on completing them one by one. Research shows this reduces cognitive load and improves focus.",
                "Use time blocking: dedicate uninterrupted blocks of time to this task to ensure progress without distractions.",
                "Work on this task during your peak productivity hours. Studies suggest most people are most focused mid-morning or early afternoon.",
                "Eliminate distractions like phone notifications or social media to maximize output."
            ],
            "medium_urgency": [
                "Prioritize this task using the Eisenhower Matrix: Do it now if it’s important, delegate or defer if it’s less critical.",
                "Set up milestones for the task over the next few days to ensure steady progress.",
                "Reward yourself after completing a specific milestone to stay motivated.",
                "Batch similar tasks together if possible to maintain a productive flow."
            ],
            "low_urgency": [
                "Plan this task using spaced repetition: Spread out work sessions to allow for better retention and reduced burnout.",
                "Focus on smaller subtasks to make incremental progress. Studies show small wins boost motivation.",
                "Schedule this task during low-energy periods of your day, like after lunch or late afternoon.",
                "Revisit your plan weekly to ensure the task stays on track and doesn’t become urgent."
            ],
            "important": [
                "Ensure a distraction-free environment, as important tasks require high cognitive focus.",
                "Use the Pomodoro technique: Work in 25-minute intervals followed by a short break to sustain energy levels.",
                "Communicate with your team or peers if collaboration can enhance the task’s outcome.",
                "Review the task requirements twice to avoid mistakes, as errors in important tasks can have significant consequences."
            ],
            "less_important": [
                "Handle this task during downtime or low-energy periods, as it’s less critical.",
                "Combine this task with routine activities to maximize efficiency.",
                "Delegate or automate parts of this task, if possible, to free up time for more critical tasks.",
                "Keep this task in your peripheral focus and revisit it when higher-priority work is done."
            ]
        }

    def get_recommendation(self, urgency, importance):
        if urgency <= 2:  # High urgency
            recommendation = random.choice(self.recommendations["high_urgency"])
        elif 3 <= urgency <= 7:  # Medium urgency
            recommendation = random.choice(self.recommendations["medium_urgency"])
        else:  # Low urgency
            recommendation = random.choice(self.recommendations["low_urgency"])
        
        # Add importance-based suggestions
        if importance >= 4:
            importance_recommendation = random.choice(self.recommendations["important"])
        else:
            importance_recommendation = random.choice(self.recommendations["less_important"])
        
        return f"{recommendation} Additionally: {importance_recommendation}"

