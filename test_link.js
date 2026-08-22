import { joinSegments, pathToRoot } from "./node_modules/@quartz-community/utils/dist/path.js";

// the link is: filename.pdf
const link = "filename.pdf";
const currentSlug = "SP2026-VNAV-CourseContent/lectures/index";

// in transformLink:
// if it's a local file, and it doesn't match a markdown file, it might just use it as is?
// Let's just grep the html for the actual a tag.
