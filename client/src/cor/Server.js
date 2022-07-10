import { useContext } from "react";
import { Context } from "./Context";

function Server() {
	const context = useContext(Context);
	if (typeof context === "undefined") {
		throw new Error(">>> useKafka must be used within a kafkaContext <<<");
	}
	return context;
}

export default Server;
