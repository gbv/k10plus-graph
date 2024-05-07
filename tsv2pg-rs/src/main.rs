use std::collections::hash_set;

fn main() {
    let mut unique = hash_set::HashSet::new();
    let input = std::io::stdin();
    for line in input.lines() {
        let line2 = &line.unwrap();
        let mut data = line2.trim().split('\t');
        let ppn = data.next().unwrap().to_string();
        let sym = data.next().unwrap();
        let id = data.next().unwrap();
        if !unique.contains(&ppn) {
            println!("{} :Title", ppn);
            unique.insert(ppn.clone());
        }
        println!("'{}:{}' :Concept id:'{}'", sym, id, id);
        println!("{} -> '{}:{}' :Subject", ppn, sym, id);
    }
}
