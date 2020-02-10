<template>
  <div :class="grid" class="w-full md:w-1/2 p-6 m-2 bg-white shadow-md rounded-lg">
    <h1 class="text-4xl font-bold">
      <router-link :to="'/post/' + article.id">{{ article.title }}</router-link>
    </h1>
    <p
      class="text-gray-500"
      v-if="article.content.length > 124"
    >{{ article.content.substring(0, 124) }}...</p>
    <p class="text-gray-500" v-else>{{ article.content }}</p>
    <div class="flex justify-between items-baseline pt-12">
      <span class>
        <p class="text-gray-600">By {{ article.user }}</p>
        <p class="text-gray-600">{{ article.date_posted }}</p>
      </span>
      <button @click="isBookmarked = !isBookmarked" class="bookmark-btn p-2 rounded-full hover:bg-teal-100 focus:outline-none">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          :fill="isBookmarked ? '#4FD1C5' : 'none'"
          stroke="#4FD1C5"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="feather feather-bookmark"
        >
          <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["grid", "article"],
  data() {
    return {
      isBookmarked: false
    }
  }
};
</script>

<style lang="scss" scoped>
.bookmark-btn {
  transition: 0.2s;
}
</style>