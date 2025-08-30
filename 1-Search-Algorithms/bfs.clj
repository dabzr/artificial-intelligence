; Breadth-First-Search Algorithm

(defn bfs [graph]
  (loop [queue (conj clojure.lang.PersistentQueue/EMPTY :S)
         visited #{}
         paths {:S [:S]}]
    (if (empty? queue)
      nil
      (let [node (peek queue)
            queue (pop queue)]
        (cond
          (= node :G) (get paths node)
          :else
          (let [neighbors (remove visited (get graph node))
                visited (into visited neighbors)
                queue (into queue neighbors)
                paths (reduce (fn [m n] (assoc m n (conj (paths node) n))) paths neighbors)]
            (recur queue visited paths)))))))

(def problem {:S [:A :B] :A [:B] :B [:G :A] :G []})

(println (bfs problem)) 


