<template>
  <header class="blog-header">
    <div class="container">
      <div class="header-content">
        <h1 class="blog-title">
          <a href="/">Mike's Blog</a>
        </h1>
        <p class="blog-description">A modern Vue3 + Django blog</p>
      </div>
    </div>
  </header>
</template>

<style scoped>
.blog-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 60px 0;
  text-align: center;
}

.blog-title {
  font-size: 3rem;
  margin-bottom: 10px;
  font-weight: 700;
}

.blog-title a {
  color: white;
  text-decoration: none;
  transition: opacity 0.3s ease;
}

.blog-title a:hover {
  opacity: 0.8;
}

.blog-description {
  font-size: 1.2rem;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .blog-header {
    padding: 40px 0;
  }
  
  .blog-title {
    font-size: 2rem;
  }
  
  .blog-description {
    font-size: 1rem;
  }
}
</style>