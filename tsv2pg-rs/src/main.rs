use std::collections::hash_set;

fn main() {
    let mut unique = hash_set::HashSet::new();
    let input = std::io::stdin();
    for (index, line) in input.lines().enumerate() {
        let line2 = &line.unwrap();
        let mut data = line2.trim().split('\t');
        let ppn = data.next().unwrap().to_string();
        let sym = data.next().unwrap();
        let id = data.next().unwrap();
        if !unique.contains(&ppn) {
            println!("{} :title", ppn);
            unique.insert(ppn.clone());
        }
        println!(
            "{} -> 'http://uri.gbv.de/terminology/{}/{}' :subject",
            ppn, sym, id
        );
    }
}
