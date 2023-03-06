const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  assetsDir: "static",
  devServer: {
    proxy: {
      "/": {
        target: 'http://127.0.0.1:8000',
        ws: true,
        changeOrigin: true,
        pathRewrite: {
          '^/': ''
        }
      },
    }
  }
})
