from flask import Flask

app = Flask(__name__)


@app.route('/')
def greeting():
    return f''' <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <title>Lana Del Rey</title>
</head>
<body>
<h1> Lana Del Rey's best albums</h1>
<div id="sliderBigImages" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="rounded mx-auto d-block" src="/static/img/burn.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="rounded mx-auto d-block" src="/static/img/paradise.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="rounded mx-auto d-block" src="/static/img/ultra.jpg" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#sliderBigImages" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="btn btn-primary"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#sliderBigImages" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="btn btn-primary"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<!-- подключение JavaScript -->
    <!-- Сначала jQuery, затем Bootstrap JS, а Popper.js подключать необязательно -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
    integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')