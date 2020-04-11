from flask import Flask,render_template,request,redirect,url_for


app= Flask(__name__)

posts={
  0: {
      'title': 'Hi',
      'content': 'My first blog post'
     }}



@app.route("/")# always home page...this decorator will work on this Function
#User run the app and browser asks for home page and run function associate with a particular route
def home():
    return render_template('home.html', post=posts)#Flask endpoint

@app.route("/post/<int:post_id>") #post/0
def post(post_id):
    post=posts.get(post_id)
    if not post:# If the get method do not get anything it return none
       return render_template('404.html', message=f"No Post exists with id {post_id}")
    return render_template('post.html', post=post)



@app.route('/post/create',methods=['POST','GET'])
def create():
    #post attaches the data payload to the request instead of adding in the query string
    #get request can not have data payload-done by browser
    if request.method=='POST':
        title=request.form.get('title')
        print(title)
        content=request.form.get('content')
        print(content)
        post_id=len(posts)
        posts[post_id]={'title': title,
                        'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html')

if __name__=="__main__":
      app.run(debug=True)#gives information if something go wrong


