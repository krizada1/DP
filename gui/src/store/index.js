import Vue from 'vue'
import Vuex from 'vuex'


import { return_plot } from '@/assets/js/my'


Vue.use(Vuex)

export default new Vuex.Store({
    strict: false,

    state: {
        plotly_data: {},
        plotly_payload: {},
        plotly_payload_numberofrecords: { pocet_zaznamu: 12 },
        table_data: {},
    },

    mutations: {
        mutate_plotly_data(state, { payload }) {
            state.plotly_data = payload
        },
        mutate_plotly_payload(state, { payload }) {
            state.plotly_payload = payload
        },
        mutate_plotly_payload_numberofrecords(state, { payload }) {
            state.plotly_payload_numberofrecords = payload
        },
        mutate_table_data(state, { payload }) {
            state.table_data = payload
        },
    },

    actions: {
        get_plot({ commit }) {

            window.eel.get_plot("/DriveVsa/Drive/r0035[u1]", "/DriveVsa/Drive/r0035[u2]", 100, "Timing")((result) => {
                if (result) {
                    commit('mutate_plotly_data', { payload: return_plot(result) })
                }

            })
        },
    },
    modules: {
    },
})
