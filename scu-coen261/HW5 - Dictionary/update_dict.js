const key = head;
const value = tail;

const insert_dict = (item,dict) => pair(item, dict);

function build_dict(list) {
  return is_null(list) ? null : insert_dict(head(list), build_dict(tail(list)));
}

const lookup = dict => k => !is_null(dict) && 
                            (key(head(dict)) === k ? value(head(dict)) :
                                                     lookup(tail(dict))(k));

// const update_value = dict => k => v => !is_null(dict) && 
//                             (key(head(dict)) === k ? value(head(dict)) :
//                                                      lookup(tail(dict)(k)));

const build_updated_dict = dict => (k, v) => {
  return is_null(dict) ? null 
  : key(head(dict)) === k
    ? insert_dict(pair(k, v), build_dict(tail(dict))) 
    : insert_dict(head(dict), build_dict(tail(dict)));
};
                                                     
                                                     
// const update_dict = dict => (k, v) => lookup(dict)(k) ? update_value(dict)(k)(v) : insert_dict(k, v)(dict);
const hungarian = build_dict(list(pair(1, "egy"), pair(2, "ketto"), pair(3, "harom")));

// hungarian;
// lookup(hungarian)(7);
build_updated_dict(hungarian)(3, "milo");
