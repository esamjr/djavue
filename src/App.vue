<template>
  <div id="app">
    <div id="nav">
      <div class="upper p-5 bg-white shadow-md">
        <div class="container mx-auto">
          <div class="flex justify-between items-baseline">
            <h1 class="text-2xl font-bold">
              <router-link to="/" class="brand text-teal-400">Djavue</router-link>
            </h1>
            <div class="flex items-baseline">
              <a href="#" class="px-2">
                <img src="@/assets/icons/search.svg" alt />
              </a>
              <a href="#" class="px-2">
                <img src="@/assets/icons/bookmark.svg" alt />
              </a>
              <a href="#" class="px-2 mr-5">
                <img src="@/assets/icons/bell.svg" alt />
              </a>
              <button class="px-4 py-1 bg-transparent border-2 border-teal-400 text-teal-400 rounded focus:outline-none">
                Upgrade
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="bottom p-3 mb-12 bg-teal-100 shadow-md">
        <div class="container mx-auto">
          <div class="flex justify-around items-baseline text-gray-500">
            <a href="#" class="text-sm text-teal-800 font-thin">HOME</a>
            <a href="#" class="text-sm text-teal-800 font-thin">CATEGORY</a>
            <a href="#" class="text-sm text-teal-800 font-thin">TRENDING</a>
            <a href="#" class="text-sm text-teal-800 font-thin">SUBSCRIPTION</a>
            <a href="#" class="text-sm text-teal-800 font-thin">CONTACT</a>
          </div>
        </div>
      </div>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
body {
  background: #f5f5f5;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#nav {
  .brand {
    font-family: "Gilroy", sans-serif;
  }
}
</style>
