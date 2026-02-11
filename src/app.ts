
export const handler = async (event: any) => {
    try {
        console.log(event);

        return {
            statusCode: 200,
            body: JSON.stringify({
                status: "success",
                message: "handler triggered"
            })
        }
    } catch (error) {
        const errorMessage = error instanceof Error ? error.message : "Something went wrong";
        console.error(errorMessage);
        return {
            statusCode: 500,
            body: JSON.stringify({
                status: "failed",
                message: "Something went wrong"
            }),
        };
    }
}