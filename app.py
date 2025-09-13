from flask import Flask, render_template

app = Flask(__name__)

# List of slides: each has an image + message
slides = [
    {"img": "img1.jpg", "msg": "Hiiiiiii GunGun, today there are no confessions, only facts."},
    {"img": "img2.jpg", "msg": "You’re a genuinely good person.You’re absolutely the cutest."},
    {"img": "img3.jpg", "msg": "I adore your kindness and honesty 🌸,Even when you scold me, I can’t help but stay quiet, there’s a strange comfort in it."},
    {"img": "img4.jpg", "msg": "Sometimes you really annoy me… and I kind of like it. :)🙂‍↔️"},
    {"img": "img5.jpg", "msg": "(A little delusional, but true) I’m convinced you were written perfectly by God🥹, a little magic wrapped in kindness, and I fall for you more every day🥰😍."},
    {"img": "img6.jpg", "msg": "Like I said, my attitude will always stay the same for you, and only you."},
    {"img": "img7.jpg", "msg": "I know the last few days were rough, you were upset with me and I’m really sorry. When you started ignoring me and became quiet, I felt so sad and frustrated, but I figured you must be stressed too, so I didn’t push. When you finally talked to me again, I felt like the happiest person on earth like something wonderful had come back into my life."}
]

@app.route("/")
def home():
    return render_template("index.html", slides=slides)

if __name__ == "__main__":
    app.run(debug=True)
