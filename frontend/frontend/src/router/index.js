import Vue from 'vue'
import VueRouter from 'vue-router'
import ChatBot from "../components/ChatBot.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "ChatBot",
    component: ChatBot
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
