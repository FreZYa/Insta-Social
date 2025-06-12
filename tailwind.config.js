module.exports = {
  content: [
    './users/templates/**/*.html',
    './posts/templates/**/*.html',
    './templates/**/*.html',
    './users/static/**/*.js',
    './posts/static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'social-blue': '#1da1f2',
        'social-gray': '#f7f9fa',
      }
    },
  },
  plugins: [],
} 