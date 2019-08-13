import flask

app = flask.Flask(__name__)


def get_task_data():
    return [
        {
            "action": "next",
            "title": "Update tasks list",
            "description": "review list",
            "waiting": "Tom",
            "tag": "work",
        },
        {
            "action": "waiting",
            "title": "Waiting for someone",
            "description": "who am I waiting for",
            "waiting": "Mark",
            "tag": "work",
        },
        {
            "action": "next",
            "title": "Review proposals",
            "description": "Tom has list on desk",
            "tag": "project 1",
        },
    ]


@app.route("/")
@app.route("/tasks")
def tasks():
    tasks = get_task_data()
    # return {"tasks": tasks}
    return flask.render_template("tasks/tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
