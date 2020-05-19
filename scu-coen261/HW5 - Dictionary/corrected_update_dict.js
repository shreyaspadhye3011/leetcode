const key = head;
const value = tail;

const insert_dict = (k, v) => dict => pair(pair(k, v), dict);

const build_dict = list => is_null(list) ? null :
          insert_dict(key(head(list)),value(head(list)))(build_dict(tail(list)));


const lookup = dict => k => !is_null(dict) && 
                            (key(head(dict)) === k ? value(head(dict)) :
                                                     lookup(tail(dict))(k));

const update_dict = dict => (k, v) => {
  return is_null(dict) ? null 
  : key(head(dict)) === k
    ? insert_dict(k, v)(update_dict(tail(dict))(k, v))
    : insert_dict(key(head(dict)), value(head(dict)))(update_dict(tail(dict))(k, v));
};
                                                     
                                                     
const hungarian = build_dict(list(pair(1, "egy"), pair(2, "ketto"), pair(3, "harom"), pair(2, "lib")));

// hungarian;
// lookup(hungarian)(7);
update_dict(hungarian)(2, "ammito");
