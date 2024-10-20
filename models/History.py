class History():
    def __init__(self, num_questions):
        self.num_questions = num_questions
        self.history = [{"role": "system", "content": f"You are an AI journaling assistant who asks {num_questions} questions each day ..."}]

    def add_to_history(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = [{"role": "system", "content": f"You are an AI journaling assistant who asks {self.num_questions} questions each day ..."}]
        return self.history
    
    def get_last_question(self):
        for i in range(len(self.history)-1, -1, -1):
            if self.history[i]['role'] == 'assistant':
                return self.history[i]['content']
        return None
    
    def get_last_answer(self):
        for i in range(len(self.history)-1, -1, -1):
            if self.history[i]['role'] == 'user':
                return self.history[i]['content']
        return None
    
    def get_last_role(self):
        return self.history[-1]['role']
        
    