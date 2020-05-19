const key = head;
const value = tail;

const insert_dict = (item,dict) => pair(item, dict);

function build_dict(list) {
  return is_null(list) ? null : insert_dict(head(list), build_dict(tail(list)));
}

const lookup = dict => k => !is_null(dict) && 
                            (key(head(dict)) === k ? value(head(dict)) :
                                                     lookup(tail(dict))(k));

const hungarian = build_dict(list(pair(1, "egy"), pair(2, "ketto"), pair(3, "harom")));

lookup(hungarian)(2);
