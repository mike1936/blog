import axios from 'axios'

// Create axios instance with base configuration
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// API service methods
export const blogApi = {
  // Get all posts
  getPosts: (params = {}) => api.get('/posts/', { params }),
  
  // Get single post by slug
  getPost: (slug) => api.get(`/posts/${slug}/`),
  
  // Get all categories
  getCategories: () => api.get('/categories/'),
  
  // Get all tags
  getTags: () => api.get('/tags/'),
  
  // Get blog statistics
  getStats: () => api.get('/stats/'),
  
  // Create comment
  createComment: (postSlug, commentData) => 
    api.post(`/posts/${postSlug}/comments/`, commentData),
}

export default api