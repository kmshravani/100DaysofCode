#Creating Class, Object, Attributes, Methods in a small quiz game project. 
class Question:
  def __init__(self,q_text,q_answer):
    self.text = q_text
    self.answer = q_answer

new_q = Question("Question?", "Answer")
print(new_q.text)




#PascalCase is usually used for Class names in Python
#snake_case for variables and others in Python
#attributes are variables associated with an object. Almost just like a new variable but we attach it to an object.
#Objects are instantiations of Classes.
