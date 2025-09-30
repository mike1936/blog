<script setup>
const props = defineProps({
  categories: {
    type: Array,
    default: () => []
  },
  tags: {
    type: Array,
    default: () => []
  },
  stats: {
    type: Object,
    default: () => ({})
  }
})
</script>

<template>
  <div class="sidebar">
    <!-- Blog Stats -->
    <div class="widget">
      <h3 class="widget-title">Blog Stats</h3>
      <div class="stats-grid">
        <div class="stat-item">
          <span class="stat-number">{{ stats.total_posts || 0 }}</span>
          <span class="stat-label">Posts</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">{{ stats.total_categories || 0 }}</span>
          <span class="stat-label">Categories</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">{{ stats.total_tags || 0 }}</span>
          <span class="stat-label">Tags</span>
        </div>
      </div>
    </div>

    <!-- Categories -->
    <div class="widget" v-if="categories.length > 0">
      <h3 class="widget-title">Categories</h3>
      <ul class="category-list">
        <li v-for="category in categories" :key="category.id" class="category-item">
          <a href="#" class="category-link">
            {{ category.name }}
            <span class="post-count">({{ category.posts_count || 0 }})</span>
          </a>
        </li>
      </ul>
    </div>

    <!-- Tags -->
    <div class="widget" v-if="tags.length > 0">
      <h3 class="widget-title">Tags</h3>
      <div class="tags-cloud">
        <a 
          v-for="tag in tags" 
          :key="tag.id" 
          href="#" 
          class="tag-link"
        >
          {{ tag.name }}
        </a>
      </div>
    </div>

    <!-- Recent Posts -->
    <div class="widget" v-if="stats.recent_posts && stats.recent_posts.length > 0">
      <h3 class="widget-title">Recent Posts</h3>
      <ul class="recent-posts">
        <li v-for="post in stats.recent_posts" :key="post.id" class="recent-post">
          <a :href="`#/post/${post.slug}`" class="recent-post-link">
            {{ post.title }}
          </a>
          <span class="recent-post-date">
            {{ new Date(post.published_at).toLocaleDateString() }}
          </span>
        </li>
      </ul>
    </div>

    <!-- Admin Link -->
    <div class="widget">
      <h3 class="widget-title">Admin</h3>
      <p class="admin-description">Manage your blog content</p>
      <a href="http://127.0.0.1:8000/admin/" target="_blank" class="admin-button">
        Go to Admin Panel
      </a>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.widget {
  background: white;
  border-radius: 8px;
  padding: 25px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.widget-title {
  margin-bottom: 20px;
  color: #333;
  font-size: 1.2rem;
  border-bottom: 2px solid #667eea;
  padding-bottom: 8px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}

.stat-item {
  text-align: center;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 6px;
}

.stat-number {
  display: block;
  font-size: 1.8rem;
  font-weight: bold;
  color: #667eea;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
}

.category-list {
  list-style: none;
}

.category-item {
  margin-bottom: 10px;
}

.category-link {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #333;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 4px;
  transition: background 0.3s ease;
}

.category-link:hover {
  background: #f8f9fa;
  color: #667eea;
}

.post-count {
  color: #999;
  font-size: 0.9rem;
}

.tags-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-link {
  background: #e9ecef;
  color: #495057;
  padding: 6px 12px;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.tag-link:hover {
  background: #667eea;
  color: white;
}

.recent-posts {
  list-style: none;
}

.recent-post {
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.recent-post:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.recent-post-link {
  display: block;
  color: #333;
  text-decoration: none;
  font-weight: 500;
  margin-bottom: 5px;
  line-height: 1.4;
  transition: color 0.3s ease;
}

.recent-post-link:hover {
  color: #667eea;
}

.recent-post-date {
  color: #999;
  font-size: 0.8rem;
}

.admin-description {
  color: #666;
  margin-bottom: 15px;
  font-size: 0.9rem;
}

.admin-button {
  display: inline-block;
  background: #28a745;
  color: white;
  padding: 10px 16px;
  text-decoration: none;
  border-radius: 5px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background 0.3s ease;
}

.admin-button:hover {
  background: #218838;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .stat-item {
    padding: 10px;
  }
  
  .stat-number {
    font-size: 1.5rem;
  }
}
</style>