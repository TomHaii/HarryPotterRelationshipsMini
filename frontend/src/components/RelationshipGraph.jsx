import Graph from "graphology";
import {
  SigmaContainer,
  ControlsContainer,
  ZoomControl,
  SearchControl,
  FullScreenControl,
} from "@react-sigma/core";
import "@react-sigma/core/lib/react-sigma.min.css";
import "./RelationshipGraph.css";
import { capitalizeFirstLetterOfName } from "../utils/StringUtils";

const RED = "#FA4F40";
const BLUE = "#727EE0";

export const RelationshipGraph = ({ character, characterRelationships }) => {
  const graph = new Graph();
  graph.addNode(character, {
    x: 0,
    y: 0,
    size: 15 * 5,
    label: character,
    color: RED,
  });
  characterRelationships.forEach((n) => {
    const score = n[1];
    if (score > 0) {
      graph.addNode(n[0], {
        x: 0,
        y: 0,
        size: n[1] * 3,
        label: capitalizeFirstLetterOfName(n[0]),
        color: BLUE,
      });
      graph.addEdge(character, n[0]);
    }
  });

  graph.nodes().forEach((node, i) => {
    if (node == character) {
      return;
    }
    const angle = (i * 2 * Math.PI) / graph.order;
    graph.setNodeAttribute(node, "x", 100 * Math.cos(angle));
    graph.setNodeAttribute(node, "y", 100 * Math.sin(angle));
  });

  console.log(character);
  return (
    <SigmaContainer
      graph={graph}
      style={{
        height: "1000px",
        width: "100%",
        margin: "0",
        padding: "0",
      }}
    >
      <ControlsContainer
        position={"bottom-right"}
        style={{ marginLeft: "500px" }}
      >
        <ZoomControl />
        <FullScreenControl />
      </ControlsContainer>
      <ControlsContainer position={"top-right"}>
        <SearchControl />
      </ControlsContainer>
    </SigmaContainer>
  );
};
