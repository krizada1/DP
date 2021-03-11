let devtool_mode
if (process.env.NODE_ENV === 'development') {
  devtool_mode = 'source-map';
} else {
  devtool_mode = false;
}

module.exports = {
  outputDir: "web_builded",
  transpileDependencies: [
    'vuetify'
  ],
  productionSourceMap: process.env.NODE_ENV != 'production',

  configureWebpack: {
    devtool: devtool_mode,
  }
}
