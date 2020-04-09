from flask import Flask,render_template


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
    if not post:# If the get method do not get anything it return none
       return render_template('404.html', message=f"No Post exists with id {post_id}")
    return render_template('post.html', post=post)



if __name__=="__main__":
      app.run(debug=True)#gives information if something go wrong


