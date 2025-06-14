<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${page_title or "FastAPI App"}</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="/">Meeting Assistant</a>
    </div>
  </nav>
  ${next.body()}
  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>