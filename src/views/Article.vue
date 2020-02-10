<template>
  <div class="home container mx-auto md:px-32 lg:px-48">
    <div class="flex flex-wrap justify-center">
      <div class="w-full p-6 m-6" :class="grid">
        <h1 class="text-4xl font-bold">{{ article.title }}</h1>
        <p class="text-gray-600">By {{ article.user }}</p>
        <p class="text-gray-600">{{ article.date_posted }}</p>
        <div class="pt-12 content">{{ article.content }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Post from "@/components/Post";

export default {
  name: "Article",
  components: {
    Post
  },
  data() {
    return {
      endpoint: "/api/v1/articles/",
      article: null
    };
  },
  created() {
    this.fetchArticle();
  },
  methods: {
    async fetchArticle() {
      try {
        let response = await axios.get(
          this.endpoint + this.$route.params["id"]
        );

        this.article = response.data;
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.content {
  font-size: 20px;
}
</style>