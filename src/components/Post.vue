<template>
  <router-link
    :to="'/post/' + article.id"
    :class="grid"
    class="w-full md:w-1/2 p-6 m-2 bg-white shadow-md rounded-lg"
  >
    <h1 class="text-4xl font-bold">{{ article.title }}</h1>
    <p
      class="text-gray-500"
      v-if="article.content.length > 124"
    >{{ article.content.substring(0, 124) }}...</p>
    <p class="text-gray-500" v-else>{{ article.content }}</p>
    <div class="pt-12">
      <p class="text-gray-600">By {{ article.user }}</p>
      <p class="text-gray-600">{{ article.date_posted }}</p>
    </div>
  </router-link>
</template>

<script>
export default {
  props: ["grid", "article"]
};
</script>

<style>
</style>