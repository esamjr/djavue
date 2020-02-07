<template>
  <div class="w-full md:w-1/2 p-6 m-6 bg-white shadow-md rounded-lg" :class="grid">
    <h1 class="text-5xl font-bold">
      <router-link :to="'/post/' + article.id">{{ article.title }}</router-link>
    </h1>
    <p>{{ article.content }}</p>
    <div class="pt-12">
      <p class="text-gray-600">By {{ article.user }}</p>
      <p class="text-gray-600">{{ article.date_posted }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["grid", "article"]
};
</script>

<style>
</style>