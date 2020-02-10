<template>
  <div class="home container mx-auto">
    <h1 class="text-5xl font-bold">Blog</h1>
    <div class="flex flex-wrap">
      <Post :article="article" />
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
      let response = await axios.get(this.endpoint + this.$route.params["id"]);

      this.article = response.data[0];
    }
  }
};
</script>

<style>
</style>