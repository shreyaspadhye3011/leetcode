const key = head;
const value = tail;
const insert_dict = (k, v) => dict => pair(pair(k, v), dict);

const build_dict = list => is_null(list) ? null :
          insert_dict(key(head(list)),value(head(list)))(build_dict(tail(list)));

const lookup = dict => k => !is_null(dict) &&
                        	(key(head(dict)) === k ? value(head(dict)) :
                                             	   lookup(tail(dict))(k));
// const update_dict = dict => (k, v) => ???;

const hungarian_words = build_dict(list(pair(1, "egy"), pair(2, "kettõ"), pair(3, "három")));

const hungarian = lookup(hungarian_words);

hungarian(3);
