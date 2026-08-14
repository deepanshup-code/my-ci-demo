from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI Demo Application</h1>
    <p>Running from Docker image published to GHCR.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print("CI Demo Application")
    print("2 + 3 =", add(2, 3))
    print("2 * 3 =", multiply(2, 3))

print("CI Demo Application v2")
print("CI Demo Application v3")
print("CI Demo Application v4")
