import store from '@/store'


export function mutate(property, value) {

  store.commit("shared/mutate", [property, value])
}

export function create_allert(py_caption, py_message, py_error = '') {

  store.commit("shared/allert", { caption: py_caption, message: py_message, error: py_error })

}




// import { clear_content } from './my'

// export function add_HTML_element(content, into_paragraph, id_parent, id_created, caption, replace = 0, added_class = "added") {

//   if (replace) {
//     clear_content(id_parent);
//   }

//   var new_div = document.createElement('div');
//   new_div.id = id_created;
//   if (typeof added_class == "string") {
//     new_div.classList.add(added_class);
//   } else {
//     new_div.classList.add(...added_class);
//   }

//   if (into_paragraph) {
//     var new_p = document.createElement('p');
//     new_p.innerHTML = content;
//     new_div.appendChild(new_p);
//   } else {
//     new_div.innerHTML = content;
//   }

//   if (caption) {
//     var new_caption = document.createElement('p');
//     new_caption.innerHTML = caption;
//     new_caption.classList.add("my-caption");
//     document.getElementById(id_parent).appendChild(new_caption);
//   }

//   document.getElementById(id_parent).appendChild(new_div);
// }
