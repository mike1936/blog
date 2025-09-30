<script setup>
import { ref, onMounted } from 'vue'
import { blogApi } from './services/api.js'
import BlogHeader from './components/BlogHeader.vue'
import PostList from './components/PostList.vue'
import BlogSidebar from './components/BlogSidebar.vue'

const posts = ref([])
const categories = ref([])
const tags = ref([])
const stats = ref({})
const loading = ref(true)
const error = ref(null)

const loadBlogData = async () => {
  try {
    loading.value = true
    const [postsRes, categoriesRes, tagsRes, statsRes] = await Promise.all([
      blogApi.getPosts(),
      blogApi.getCategories(),
      blogApi.getTags(),
      blogApi.getStats()
    ])
    
    posts.value = postsRes.data.results || postsRes.data
    categories.value = categoriesRes.data
    tags.value = tagsRes.data
    stats.value = statsRes.data
  } catch (err) {
    error.value = 'Failed to load blog data'
    console.error('Error loading blog data:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadBlogData()
})
</script>

<template>
  <div id="app">
    <BlogHeader />
    
    <main class="main-content">
      <div class="container">
        <div class="content-wrapper">
          <div class="posts-section">
            <div v-if="loading" class="loading">
              <p>Loading blog posts...</p>
            </div>
            
            <div v-else-if="error" class="error">
              <p>{{ error }}</p>
            </div>
            
            <div v-else>
              <PostList :posts="posts" />
            </div>
          </div>
          
          <aside class="sidebar">
            <BlogSidebar 
              :categories="categories"
              :tags="tags"
              :stats="stats"
            />
          </aside>
        </div>
      </div>
    </main>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  color: #333;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.main-content {
  padding: 40px 0;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 40px;
}

.loading, .error {
  text-align: center;
  padding: 40px;
  font-size: 18px;
}

.error {
  color: #dc3545;
}

@media (max-width: 768px) {
  .content-wrapper {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .sidebar {
    order: -1;
  }
}
</style>
