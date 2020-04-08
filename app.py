from flask import Flask


app= Flask(__name__)

posts={
  0: {
      'title': 'Hi',
      'content': 'My first blog post'
     }}



@app.route("/")# always home page...this decorator will work on this Function
#User run the app and browser asks for home page and run function associate with a particular route
def home():
    return "Hello, My name is Jaskiran!"#Flask endpoint

@app.route("/post/<int:post_id>") #post/0
def post(post_id):
    post=posts.get(post_id)
    return f"Post {post['title']}, content:\n\n {post['content']}"


if __name__=="__main__":
      app.run(debug=True)#gives information if something go wrong


