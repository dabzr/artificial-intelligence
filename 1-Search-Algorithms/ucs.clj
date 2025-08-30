; Uniform-Cost-Search Algorithm

(defn ucs [graph]
  (loop [priority-queue [[[:S] 0]]] ;; cada elemento é [caminho custo]
    (let [[[path cost] & rest-pq] (sort-by second priority-queue)
          node (last path)
          neighbors (get graph node)]
      (if (= node :G)
        path
        (let [new-nodes (map (fn [[nd cs]] [(conj path nd) (+ cost cs)]) neighbors)]
          (recur (into rest-pq new-nodes)))))))

(def problem {:S [[:A 5] [:B 2]]
              :A [[:B 1]]
              :B [[:G 7]]
              :G []})

(println (ucs problem)) 

