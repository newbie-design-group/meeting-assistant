<%inherit file="base.mako"/>
<%page args="request, page_title=None, error=None"/>
<%block name="body">
<div class="container mt-5">
  <h2 class="text-center mb-4">${page_title or "Sign Up"}</h2>
  % if error:
    <div class="alert alert-danger">${error}</div>
  % endif
  <form method="post" action="/signup">
    <div class="mb-3">
      <label class="form-label" for="username">Username</label>
      <input class="form-control" id="username" name="username" required />
    </div>
    <div class="mb-3">
      <label class="form-label" for="email">Email</label>
      <input type="email" class="form-control" id="email" name="email" required />
    </div>
    <div class="mb-3">
      <label class="form-label" for="password">Password</label>
      <input type="password" class="form-control" id="password" name="password" required />
    </div>
    <div class="mb-3">
      <label class="form-label" for="confirm">Confirm Password</label>
      <input type="password" class="form-control" id="confirm" name="confirm" required />
    </div>
    <button type="submit" class="btn btn-primary w-100">Create Account</button>
  </form>
</div>
</%block>