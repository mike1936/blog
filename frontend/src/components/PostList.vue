<script setup>
import { computed } from 'vue'

const props = defineProps({
  posts: {
    type: Array,
    default: () => []
  }
})

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString(undefined, options)
}

const hasRecentPosts = computed(() => props.posts && props.posts.length > 0)
</script>

<template>
  <div class="posts-container">
    <h2 class="section-title">Recent Posts</h2>
    
    <div v-if="!hasRecentPosts" class="no-posts">
      <div class="no-posts-content">
        <h3>No posts yet!</h3>
        <p>Check back soon for new content, or visit the admin panel to add some posts.</p>
        <a href="http://127.0.0.1:8000/admin/" target="_blank" class="admin-link">
          Go to Admin Panel
        </a>
      </div>
    </div>
    
    <div v-else class="posts-grid">
      <article 
        v-for="post in posts" 
        :key="post.id" 
        class="post-card"
      >
        <div class="post-image" v-if="post.featured_image">
          <img :src="post.featured_image" :alt="post.title" />
        </div>
        
        <div class="post-content">
          <h3 class="post-title">
            <a :href="`#/post/${post.slug}`">{{ post.title }}</a>
          </h3>
          
          <div class="post-meta">
            <span class="post-author">By {{ post.author }}</span>
            <span class="post-date">{{ formatDate(post.published_at) }}</span>
            <span v-if="post.category" class="post-category">
              in {{ post.category.name }}
            </span>
          </div>
          
          <p class="post-excerpt">{{ post.excerpt }}</p>
          
          <div class="post-tags" v-if="post.tags && post.tags.length">
            <span 
              v-for="tag in post.tags" 
              :key="tag.id" 
              class="tag"
            >
              {{ tag.name }}
            </span>
          </div>
          
          <div class="post-footer">
            <a :href="`#/post/${post.slug}`" class="read-more">Read More</a>
            <span class="comments-count">
              {{ post.comments_count || 0 }} comments
            </span>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.posts-container {
  margin-bottom: 40px;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 30px;
  color: #333;
  border-bottom: 2px solid #667eea;
  padding-bottom: 10px;
}

.no-posts {
  text-align: center;
  padding: 60px 20px;
  background: #f8f9fa;
  border-radius: 8px;
}

.no-posts-content h3 {
  color: #666;
  margin-bottom: 15px;
  font-size: 1.5rem;
}

.no-posts-content p {
  color: #888;
  margin-bottom: 20px;
  font-size: 1.1rem;
}

.admin-link {
  display: inline-block;
  background: #667eea;
  color: white;
  padding: 12px 24px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: 500;
  transition: background 0.3s ease;
}

.admin-link:hover {
  background: #5a6fd8;
}

.posts-grid {
  display: grid;
  gap: 30px;
}

.post-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}

.post-image {
  height: 200px;
  overflow: hidden;
}

.post-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.post-content {
  padding: 25px;
}

.post-title {
  margin-bottom: 15px;
  font-size: 1.4rem;
}

.post-title a {
  color: #333;
  text-decoration: none;
  transition: color 0.3s ease;
}

.post-title a:hover {
  color: #667eea;
}

.post-meta {
  margin-bottom: 15px;
  font-size: 0.9rem;
  color: #666;
}

.post-meta span {
  margin-right: 15px;
}

.post-excerpt {
  margin-bottom: 20px;
  color: #666;
  line-height: 1.6;
}

.post-tags {
  margin-bottom: 20px;
}

.tag {
  display: inline-block;
  background: #e9ecef;
  color: #495057;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-right: 8px;
  margin-bottom: 4px;
}

.post-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 15px;
  border-top: 1px solid #eee;
}

.read-more {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.read-more:hover {
  color: #5a6fd8;
}

.comments-count {
  color: #999;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.6rem;
  }
  
  .post-content {
    padding: 20px;
  }
  
  .post-footer {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
}
</style>