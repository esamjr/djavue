<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link class="mx-4" to="/create">Create</router-link>
      <router-link to="/edit">Edit</router-link>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  background: #f5f5f5;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
