const key = head;
const value = tail;
const insert_dict = (k,v) => dict => pair(pair(k,v),dict);
function build_dict(list){
    return is_null(list) ? null : insert_dict(head(list),build_dict(tail(list)));
}
const lookup = dict => k => !is_null(dict) && (key(head(dict))) === k ? value(head(dict)) : lookup(tail(dict),k);
const update_dict = dict => (k,v) => value(head(dict)) === k ? insert_dict((k,v),build_dict(tail(dict))):(head(dict),update_dict(tail(dict))(k,v));

function hash(value){
    return value%31;
}

function contains_hs(hashset,x){
    if (is_null(hashset)){
        return false;
    }
    const key = hash(x);
    const chain = lookup(hashset)(key);
    return !is_null(chain) && contains_l(chain,x);
}

function insert_hs(set,x){
    return is_null(set) ? (x,null) : head(set) === x ? set : (head(set),insert_hs(tail(set),x));
}

function union_hs(set1,set2){
    return is_null(set1) ? set2 : (head(set1),union(tail(set1),set2));
}

