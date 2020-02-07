<template>
  <div class="w-full md:w-1/2 p-6 m-6 bg-white shadow-md rounded-lg" :class="grid">
    <img :src="item.image" class="rounded-lg" />
    <h1 class="text-5xl font-bold">
      <router-link :to="'/post/' + item.id">{{ item.title }}</router-link>
    </h1>
    <p>{{ item.content }}</p>
    <div class="pt-12">
      <p class="text-gray-600">By {{ item.user }}</p>
      <p class="text-gray-600">{{ item.date_posted }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["grid", "item"]
};
</script>

<style>
</style>