import Vue from 'vue'
import Vuex from 'vuex'

import { return_plot } from '@/assets/js/my'


Vue.use(Vuex)

export default new Vuex.Store({
  strict: false,

  state: {
    plotly_data: {}
  },

  mutations: {
    mutate_plotly_data(state, { payload }) {
      state.plotly_data = payload

    },
  },

  actions: {
    get_plot({ commit }) {

      window.eel.get_plot()((result) => {
        if (result) {
          commit('mutate_plotly_data', { payload: return_plot(result) })
        }

      })


    },
  },
  modules: {
  }
})
